from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
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
    image = CloudinaryField('image', default='palceholder')
    description = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default='admin', related_name='game_post')
    genre = models.CharField(max_length=80, choices=GENRES, default=SHOOTER)
    release_date = models.CharField(max_length=20)
    platform = models.CharField(max_length=15, choices=GAMING_PLATFORM, default=ALL)
    likes = models.ManyToManyField(User, related_name='game_likes', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        # is it possible to use release date instead?

    def __str__(self):
        return self.title

    # add likes later
