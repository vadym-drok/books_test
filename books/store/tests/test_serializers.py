from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg
from django.test import TestCase
from store.serializers import BooksSerializer
from store.models import Book, UserBookRelation


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')
        book_1 = Book.objects.create(name='1 book', price=23, author_name='Vadym')
        book_2 = Book.objects.create(name='book2', price=53, author_name='Vadym')

        UserBookRelation.objects.create(user=user1, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=user2, book=book_1, like=True, rate=3)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True, rate=5)

        UserBookRelation.objects.create(user=user1, book=book_2, like=True, rate=5)
        UserBookRelation.objects.create(user=user2, book=book_2, like=True, rate=5)
        UserBookRelation.objects.create(user=user3, book=book_2, like=False)

        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
        ).order_by('id')
        data = BooksSerializer(books, many=True).data
        exprected_data = [
            {
                'id': book_1.id,
                'name': '1 book',
                'price': '23.00',
                'author_name': 'Vadym',
                'likes_count': 3,
                'annotated_likes': 3,
                'rating': '4.33'
            },
            {
                'id': book_2.id,
                'name': 'book2',
                'price': '53.00',
                'author_name': 'Vadym',
                'likes_count': 2,
                'annotated_likes': 2,
                'rating': '5.00'
            }
        ]
        self.assertEqual(data, exprected_data)
