from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
        user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add users to teams
        team1.members.add(user1)
        team2.members.add(user2)

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=150)

        # Create test workouts
        Workout.objects.create(name="Workout A", description="Description for Workout A")
        Workout.objects.create(name="Workout B", description="Description for Workout B")

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
