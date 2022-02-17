from django.utils import lorem_ipsum
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model

from random import randint

from ..models import Plaza, Post, Comment

User = get_user_model()


def create_plaza(**kwargs):
    """
    Create a new plaza for tests. Can be called with no arguments
    and will generate a random plaza name and slug
    :param kwargs:
    :return: Plaza
    """
    # Static counter (for uniqueness)
    if not hasattr(create_plaza, 'counter'):
        create_plaza.counter = 0
    create_plaza.counter += 1

    name = kwargs.pop("name", None)
    slug = kwargs.pop("slug", None)
    description = kwargs.pop("description", "")
    permissions = kwargs.pop("permissions", "{}")

    if name is None:
        name = f"Plaza {create_plaza.counter} {get_random_string(length=5)}"

    if slug is None:
        slug = name.lower().replace(" ", "-")

    new_plaza = Plaza.objects.create(
        name=name,
        slug=slug,
        description=description,
        permissions=permissions,
        **kwargs,
    )

    return new_plaza


def create_post(**kwargs):
    """
    Create a new post for tests. Can be called with no arguments
    and will generate a random post title, content and select the
    first plaza, user and profile
    :param kwargs:
    :return: Post
    """
    user = kwargs.pop("user", None)
    profile = kwargs.pop("profile", None)
    title = kwargs.pop("title", None)
    plaza = kwargs.pop("plaza", None)
    content = kwargs.pop("content", None)
    permissions = kwargs.pop("permissions", "{}")
    reactions = kwargs.pop("reactions", "{}")

    if user is None:
        user = User.objects.all().first()

    if profile is None:
        profile = user.profile.first()

    if title is None:
        title = get_random_string(length=randint(10, 24))

    if plaza is None:
        plaza = Plaza.objects.all().first()

    if content is None:
        content = lorem_ipsum.words(randint(24, 64), common=False)

    new_post = Post.objects.create(
        user=user,
        profile=profile,
        title=title,
        plaza=plaza,
        content=content,
        permissions=permissions,
        reactions=reactions,
        **kwargs,
    )

    created_at = kwargs.pop("created_at", None)
    if created_at is not None:
        new_post.created_at = created_at
        new_post.save()

    return new_post


def create_comment(**kwargs):
    """
    Create a new post for tests. Can be called with no arguments
    and will generate a random post title, content and select the
    first plaza, user and profile
    :param kwargs:
    :return: Post
    """
    post = kwargs.pop("post", None)
    user = kwargs.pop("user", None)
    profile = kwargs.pop("profile", None)
    content = kwargs.pop("content", None)
    reactions = kwargs.pop("reactions", "{}")

    if post is None:
        post = Post.objects.all().first()

    if user is None:
        user = User.objects.all().first()

    if profile is None:
        profile = user.profile.first()

    if content is None:
        content = lorem_ipsum.words(randint(24, 64), common=False)

    new_comment = Comment.objects.create(
        user=user,
        profile=profile,
        post=post,
        content=content,
        reactions=reactions,
        **kwargs,
    )

    created_at = kwargs.pop("created_at", None)
    if created_at is not None:
        new_comment.created_at = created_at
        new_comment.save()

    return new_comment
