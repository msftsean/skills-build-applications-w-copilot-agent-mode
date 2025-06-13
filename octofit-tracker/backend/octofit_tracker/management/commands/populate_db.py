from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, datetime
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        ]
        db.users.insert_many(users)

        # Create teams
        teams = [
            {"_id": ObjectId(), "name": "Avengers", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Hackers", "members": [users[2]["_id"], users[3]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Create activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "run", "duration": 30, "date": datetime(2025, 6, 10)},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "walk", "duration": 45, "date": datetime(2025, 6, 11)},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "cycle", "duration": 60, "date": datetime(2025, 6, 12)},
            {"_id": ObjectId(), "user": users[3]["_id"], "activity_type": "swim", "duration": 50, "date": datetime(2025, 6, 13)},
        ]
        db.activity.insert_many(activities)

        # Create leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 120},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 110},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 130},
            {"_id": ObjectId(), "user": users[3]["_id"], "score": 125},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Create workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Run", "description": "5km run around the park"},
            {"_id": ObjectId(), "name": "Evening Yoga", "description": "1 hour of yoga"},
            {"_id": ObjectId(), "name": "Strength Training", "description": "Full body workout"},
            {"_id": ObjectId(), "name": "Cycling", "description": "20km cycling session"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
