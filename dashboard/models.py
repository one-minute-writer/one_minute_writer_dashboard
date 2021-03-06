from django.conf import settings
from django.db import models
from django.utils import timezone

# Object that is persisted to database. Takes id, total time - time up to now, total word - words up till now as parameters. Because data is chunked functionality can expand to include filtering by date.
class WritingInfo(models.Model):
    writing_id = models.IntegerField(blank=True)
    word_count = models.IntegerField(blank=True)
    time_spent = models.IntegerField(blank=True) #Time spent on writing in seconds
    created_at = models.DateTimeField(default=timezone.now)

    #set method to get all time for writing id and subtract from params value. Remainder is persisted to DB

    #set method to get all words for writing id and subtract from prams value. Remainder is persisted to DB

class WritingTotals:
    def __init__(self, writing_id, total_words, total_time_in_seconds):
        self.writing_id = writing_id
        self.total_words = total_words
        self.total_time_in_seconds = total_time_in_seconds #Time spent on writing in seconds

class DashboardMetrics:
    def __init__(self, total_words_all_time, total_time_all_time, average_words_per_minute):
        self.total_words_all_time = total_words_all_time
        self.total_time_all_time = total_time_all_time
        self.average_words_per_minute = average_words_per_minute
