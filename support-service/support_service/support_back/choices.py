from django.db import models

class Choices(models.Model):

        SERVICE_TYPES = [('1', 'Consultation'),
                         ('2', 'Repair'),
                         ('3', 'Troubleshooting'),
                         ('4', 'Service maintenance'),
                         ('5', 'I pressed something and everything broke'),
                         ('6', 'Warranty service'),
                         ('7', 'It’s because of you that everything doesn’t work for me'),
                         ]
        ORDER_TYPES = [('1', 'Consultation'),
                       ('2', 'Repair'),
                       ('3', 'Troubleshooting'),
                       ('4', 'Service maintenance'),
                       ('5', 'I pressed something and everything broke'),
                       ('6', 'Warranty service'),
                       ('7', 'It’s because of you that everything doesn’t work for me'),
                       ]
        SEVERITIES = [
                        ('1', 'Low'),
                        ('2', 'Middle'),
                        ('3', 'High'),
        ]
        RATTING_FILLED = [
                        ('1', 1),
                        ('2', 2),
                        ('3', 3),
                        ('4', 4),
                        ('5', 5),
        ]