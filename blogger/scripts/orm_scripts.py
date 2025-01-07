from datetime import timedelta
from django.utils.timezone import now


from blogger.models import Blogger,Post
from django.db.models import Count

seven_days_ago = now() - timedelta(days=7)

def run():

    blogger_1 = Blogger(name = 'Ulugbek')
    blogger_1.save()

    blogger_2 = Blogger(name= 'Mahmud')
    blogger_2.save()

    post_1 = Post(title = 'Bugun toshentda ob havo',blogger = blogger_1)
    post_1.save()
    post_2 = Post(title = 'Yangiliklar',blogger = blogger_1)
    post_2.save()

    post_3 = Post(title = 'Mashinalar',blogger = blogger_2)
    post_3.save()
    post_4 = Post(title = 'IT haqida',blogger = blogger_2)
    post_4.save()

    posts = Post.objects.filter(blogger=blogger_1)
    print(posts)

    posts_7 = Post.objects.filter(created_at__gte=seven_days_ago)
    print(posts_7)

    blogger_posts = Blogger.objects.annotate(post_count=Count('posts'))
    print(blogger_posts)

    Post.objects.filter(blogger = blogger_1).delete()
    

    