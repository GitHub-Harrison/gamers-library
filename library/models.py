from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    # tidy the below - genres/platform
    SHOOTER = 'Shooter'
    ACTION_ADV = 'Action adventure'
    MOBA = 'MOBA'
    RACING = 'Racing'
    SIM = 'Simulation'
    BR = 'Battle Royale'
    RTS = 'Real-time Strategy'
    PUZZLE_PLAT = 'Puzzle Platform'
    SPORTS = 'Sports'
    MMO = 'MMO'
    SINGLE = 'Singleplayer'
    COOP = 'Co-op'
    RPG = 'Role-playing Game'
    GENRES = [
        (SHOOTER, 'Shooter'),
        (ACTION_ADV, 'Action Adventure'),
        (MOBA, 'MOBA'),
        (RACING, 'Racing'),
        (SIM, 'Simulation'),
        (BR, 'Battle Royale'),
        (RTS, 'Real-time Strategy'),
        (PUZZLE_PLAT, 'Puzzle Platform'),
        (SPORTS, 'Sports'),
        (MMO, 'MMO'),
        (SINGLE, 'Singleplayer'),
        (COOP, 'Co-op'),
        (RPG, 'Role-playing Game'),
    ]
    ALL = 'All Platforms'
    PC = 'PC'
    PS4 = 'PS4'
    PS5 = 'PS5'
    XB1 = 'Xbox One'
    XBX = 'Xbox Series X'
    SWITCH = 'Nintendo Switch'
    GAMING_PLATFORM = [
        (ALL, 'All Platforms'),
        (PC, 'PC'),
        (PS4, 'PS4'),
        (PS5, 'PS5'),
        (XB1, 'Xbox One'),
        (XBX, 'Xbox Series X'),
        (SWITCH, 'Nintendo Switch')
    ]
    title = models.CharField(max_length=180, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_post')
    genre = models.CharField(max_length=80, choices=GENRES, default=SHOOTER)
    release_date = models.CharField(max_length=20)
    platform = models.CharField(max_length=15, choices=GAMING_PLATFORM, default=ALL)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        # alphabetical instead?

    def __str__(self):
        return self.title


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE,
#                              related_name="comments")
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     approved = models.BooleanField(default=False)
#     likes = models.ManyToManyField(
#         User, related_name='blogpost_like', blank=True)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.body} by {self.name}"
