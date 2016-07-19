from app import db, models
import datetime
from sqlalchemy import text

deletedrows = models.User.query.delete()

# u = models.User(nickname='john', email='john@email.com')
# db.session.add(u)
# db.session.commit()

# u = models.User(nickname='susan', email='susan@email.com')
# db.session.add(u)
# db.session.commit()

# users = models.User.query.all()
# print(users)

# for user in users:
#      print(user.id,user.nickname)

# a = models.User.query.get(1)
# print(a)

deletedrows = models.Post.query.delete()

# p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=a)
# db.session.add(p)
# db.session.commit()

# posts = a.posts.all()
# print(posts)

# # obtain author of each post
# for p in posts:
#     print(p.id,p.author.nickname,p.body)


# # a user that has no posts
# b = models.User.query.get(2)
# print(b)
# print(u.posts.all())

# # get all users in reverse alphabetical order
# print(models.User.query.order_by(text('nickname asc')).all())