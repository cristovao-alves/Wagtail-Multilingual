from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from django.utils import translation
from wagtail.wagtailadmin.edit_handlers import TabbedInterface, ObjectList


class TranslatedField(object):
    # if you add another language, add another field next to es_field.
    # so the first line will be like:
    # def __init__(self, en_field, fr_field, es_field, anotherLanguage_field):
    def __init__(self, en_field, fr_field, es_field):
        self.en_field = en_field
        self.fr_field = fr_field
        self.es_field = es_field
        #don't forget to add a new entry to the new language
        # self.anotherLanguage_field = anotherLanguage_field

    #The default language will be english. To change that, edit the last line
    #Also it's possible te use switch instead of if conditiion
    def __get__(self, instance, owner):
        if translation.get_language() == 'fr':
            return getattr(instance, self.fr_field)
        if translation.get_language() == 'es':
            return getattr(instance, self.es_field)
        # Add a condition to the new language. Like:
        #if translation.get_language() == 'another':
            #return getattr(instance, self.anotherLanguage_field)
        else:
            return getattr(instance, self.en_field)


class HomePage(Page):
    #the title in english isn't necessary because it already exist's on the wagtail default page model
    title_fr = models.CharField(max_length=255, null=True, blank=True)
    title_es = models.CharField(max_length=255, null=True, blank=True)

    body_en = models.TextField(max_length=255, null=True, blank=True)
    body_fr = models.TextField(max_length=255, null=True, blank=True)
    body_es = models.TextField(max_length=255, null=True, blank=True)

    #It's necessary to add all the fields that are being translated
    #these are the fields you will be accesing on the main page
    translated_title = TranslatedField(
        'title',
        'title_fr',
        'title_es',
    )
    body = TranslatedField(
        'body_en',
        'body_fr',
        'body_es',
    )

    # This is were you declare what field will be on the first panel
    # Don't forget it isn't necessary to translate all fields, like image's
    content_panels = Page.content_panels + [
        FieldPanel('body_en'),
    ]

    #Fields for the french language
    french = [
        FieldPanel('title_fr', classname="fulll"),
        FieldPanel('body_fr', classname="fulll"),
    ]

    # Fields for the spanish language
    spanish = [
        FieldPanel('title_es', classname="fulll"),
        FieldPanel('body_es', classname="fulll"),
    ]

    #to add a new panel for another language, create the following as many languages as necessary
    #language = [
        #field one
        #field two
        # ...
    #]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='English'),
        ObjectList(french, heading='French'),
        ObjectList(spanish, heading='Spanish'),
        #Add new entry
        #ObjectList(language, heading='language'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings', classname="settings"),
    ])



