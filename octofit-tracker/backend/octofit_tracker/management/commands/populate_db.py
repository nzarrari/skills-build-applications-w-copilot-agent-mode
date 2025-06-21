from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        port = settings.DATABASES['default']['PORT']
        if not port:
            port = 27017
        elif isinstance(port, str):
            port = int(port)
        host = settings.DATABASES['default']['HOST']
        client = MongoClient(host, port)
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"_id": ObjectId(), "name": "Blue Team", "members": [users[0]["_id"], users[1]["_id"], users[2]["_id"]]},
            {"_id": ObjectId(), "name": "Gold Team", "members": [users[3]["_id"], users[4]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Cycling", "duration": 60},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Crossfit", "duration": 120},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Running", "duration": 90},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "Strength", "duration": 30},
            {"_id": ObjectId(), "user": users[4]["_id"], "activity_type": "Swimming", "duration": 75},
        ]
        db.activity.insert_many(activities)

        # Insert leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 95},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 85},
            {"_id": ObjectId(), "user": users[4]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Insert workouts
        workouts = [
            {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
            {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
