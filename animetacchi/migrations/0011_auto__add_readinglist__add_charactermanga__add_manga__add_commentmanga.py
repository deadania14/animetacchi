# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReadingList'
        db.create_table(u'animetacchi_readinglist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('members', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animetacchi.Members'], null=True, blank=True)),
            ('readinglist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animetacchi.Manga'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('seq_watchlist', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'animetacchi', ['ReadingList'])

        # Adding model 'CharacterManga'
        db.create_table(u'animetacchi_charactermanga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('anime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animetacchi.Manga'], null=True, blank=True)),
            ('synopsys', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'animetacchi', ['CharacterManga'])

        # Adding model 'Manga'
        db.create_table(u'animetacchi_manga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('cover', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('displaypic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('synopsys', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('airedstart', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('airedend', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('save_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
            ('seq_manga', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'animetacchi', ['Manga'])

        # Adding M2M table for field genre on 'Manga'
        m2m_table_name = db.shorten_name(u'animetacchi_manga_genre')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('manga', models.ForeignKey(orm[u'animetacchi.manga'], null=False)),
            ('genre', models.ForeignKey(orm[u'animetacchi.genre'], null=False))
        ))
        db.create_unique(m2m_table_name, ['manga_id', 'genre_id'])

        # Adding model 'CommentManga'
        db.create_table(u'animetacchi_commentmanga', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animetacchi.Members'], null=True, blank=True)),
            ('anime', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['animetacchi.Manga'], null=True, blank=True)),
            ('added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('edited', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'animetacchi', ['CommentManga'])

        # Adding M2M table for field manga on 'Daikirailist'
        m2m_table_name = db.shorten_name(u'animetacchi_daikirailist_manga')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('daikirailist', models.ForeignKey(orm[u'animetacchi.daikirailist'], null=False)),
            ('manga', models.ForeignKey(orm[u'animetacchi.manga'], null=False))
        ))
        db.create_unique(m2m_table_name, ['daikirailist_id', 'manga_id'])

        # Adding M2M table for field manga on 'Daisukilist'
        m2m_table_name = db.shorten_name(u'animetacchi_daisukilist_manga')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('daisukilist', models.ForeignKey(orm[u'animetacchi.daisukilist'], null=False)),
            ('manga', models.ForeignKey(orm[u'animetacchi.manga'], null=False))
        ))
        db.create_unique(m2m_table_name, ['daisukilist_id', 'manga_id'])


    def backwards(self, orm):
        # Deleting model 'ReadingList'
        db.delete_table(u'animetacchi_readinglist')

        # Deleting model 'CharacterManga'
        db.delete_table(u'animetacchi_charactermanga')

        # Deleting model 'Manga'
        db.delete_table(u'animetacchi_manga')

        # Removing M2M table for field genre on 'Manga'
        db.delete_table(db.shorten_name(u'animetacchi_manga_genre'))

        # Deleting model 'CommentManga'
        db.delete_table(u'animetacchi_commentmanga')

        # Removing M2M table for field manga on 'Daikirailist'
        db.delete_table(db.shorten_name(u'animetacchi_daikirailist_manga'))

        # Removing M2M table for field manga on 'Daisukilist'
        db.delete_table(db.shorten_name(u'animetacchi_daisukilist_manga'))


    models = {
        u'animetacchi.about': {
            'Meta': {'object_name': 'About'},
            'about': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']", 'null': 'True', 'blank': 'True'}),
            'seq_about': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        },
        u'animetacchi.anime': {
            'Meta': {'object_name': 'Anime'},
            'a_airedend': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'a_airedstart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'a_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'a_displaypic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'a_genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['animetacchi.Genre']", 'symmetrical': 'False'}),
            'a_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'a_synopsys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'save_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'seq_anime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.character': {
            'Meta': {'object_name': 'Character'},
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'synopsys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.charactermanga': {
            'Meta': {'object_name': 'CharacterManga'},
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Manga']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'synopsys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.chart': {
            'Meta': {'ordering': "['year']", 'object_name': 'Chart'},
            'anime': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.commentanime': {
            'Meta': {'object_name': 'CommentAnime'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'edited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']", 'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.commentmanga': {
            'Meta': {'object_name': 'CommentManga'},
            'added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'anime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Manga']", 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'edited': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']", 'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.daikirailist': {
            'Meta': {'object_name': 'Daikirailist'},
            'anime': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Character']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manga': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Manga']", 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']"})
        },
        u'animetacchi.daisukilist': {
            'Meta': {'object_name': 'Daisukilist'},
            'anime': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Character']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manga': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Manga']", 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']"}),
            'voice_character': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.VoiceCharacter']", 'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.genre': {
            'Meta': {'object_name': 'Genre'},
            'genre_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'animetacchi.manga': {
            'Meta': {'object_name': 'Manga'},
            'airedend': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'airedstart': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'displaypic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['animetacchi.Genre']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'save_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'seq_manga': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'synopsys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.members': {
            'Meta': {'object_name': 'Members'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'm_bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'm_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'm_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'm_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'm_tagline': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'seq_members': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'animetacchi.news': {
            'Meta': {'object_name': 'News'},
            'article': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_cover': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'news': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'seq_news': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.readinglist': {
            'Meta': {'object_name': 'ReadingList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']", 'null': 'True', 'blank': 'True'}),
            'readinglist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Manga']", 'null': 'True', 'blank': 'True'}),
            'seq_watchlist': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'})
        },
        u'animetacchi.voicecharacter': {
            'Meta': {'object_name': 'VoiceCharacter'},
            'character': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['animetacchi.Character']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'synopsys': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'animetacchi.watchlist': {
            'Meta': {'object_name': 'WatchList'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Members']", 'null': 'True', 'blank': 'True'}),
            'seq_watchlist': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'watchlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['animetacchi.Anime']", 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['animetacchi']