Vazifa - 4

"Models:
    Blogger:
        Fields: name, email, created_at, updated_at
        Methods: __str__, __repr__
        Meta class, verbose_name, verbose_name_plural

    Post:
        Fields: title, content, blogger(relation), created_at, updated_at
        Methods: __str__, __repr__
        Meta class, verbose_name, verbose_name_plural

    Queries:
        1. Create 2 bloggers and 4 posts, assigning posts to bloggers.
        2. Retrieve all posts written by a specific blogger.
        3. List all posts created in the last 7 days.
        4. Find the blogger who has written the most posts.
        5. Delete all posts written by a specific blogger."
