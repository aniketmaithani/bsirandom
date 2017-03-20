# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class PasswordGeneration(models.Model):
    password_unique = models.CharField(blank=False, null=False,
                                       max_length=100, help_text='Phone Number of the Complainee')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At",)

    def __str__(self):
        return self.password_unique

    class Meta:
        verbose_name = "PasswordGeneration"
        verbose_name_plural = "PasswordsGeneration"
        ordering = ['-created_at']
