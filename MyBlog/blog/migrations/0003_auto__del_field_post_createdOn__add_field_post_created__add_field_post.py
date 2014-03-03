# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Post.createdOn'
        db.delete_column(u'blog_post', 'createdOn')

        # Adding field 'Post.created'
        db.add_column(u'blog_post', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(default='2014-01-01', auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Post.postType'
        db.add_column(u'blog_post', 'postType',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['blog.PostType']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Post.createdOn'
        db.add_column(u'blog_post', 'createdOn',
                      self.gf('django.db.models.fields.DateTimeField')(default='2014-01-01', auto_now_add=True, blank=True),
                      keep_default=False)

        # Deleting field 'Post.created'
        db.delete_column(u'blog_post', 'created')

        # Deleting field 'Post.postType'
        db.delete_column(u'blog_post', 'postType_id')


    models = {
        u'blog.post': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': "'2014-01-01'", 'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.PostType']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'tech'", 'max_length': '30'})
        }
    }

    complete_apps = ['blog']