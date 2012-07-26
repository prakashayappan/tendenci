# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ProjectName'
        db.create_table('projects_projectname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectName'])

        # Adding model 'Program'
        db.create_table('projects_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['Program'])

        # Adding model 'ProgramYear'
        db.create_table('projects_programyear', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProgramYear'])

        # Adding model 'ProjectNumber'
        db.create_table('projects_projectnumber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ProjectNumber'])

        # Adding model 'RpesaPm'
        db.create_table('projects_rpesapm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['RpesaPm'])

        # Adding model 'AccessType'
        db.create_table('projects_accesstype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['AccessType'])

        # Adding model 'ResearchCategory'
        db.create_table('projects_researchcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('projects', ['ResearchCategory'])

        # Adding model 'Project'
        db.create_table('projects_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('allow_anonymous_view', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('allow_user_view', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_member_view', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_anonymous_edit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_user_edit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('allow_member_edit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('create_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_dt', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_creator', to=orm['auth.User'])),
            ('creator_username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_owner', to=orm['auth.User'])),
            ('owner_username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('status_detail', self.gf('django.db.models.fields.CharField')(default='active', max_length=50)),
            ('tags', self.gf('tagging.fields.TagField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default=u'', unique=True, max_length=200, db_index=True)),
            ('project_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectName'], null=True, blank=True)),
            ('program_year', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProgramYear'], null=True, blank=True)),
            ('project_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ProjectNumber'], null=True, blank=True)),
            ('project_status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('principal_investigator', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('principal_investigator_company', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('participants', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rpsea_pm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.RpesaPm'], null=True, blank=True)),
            ('start_dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_dt', self.gf('django.db.models.fields.DateTimeField')()),
            ('project_abstract', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('project_abstract_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('project_fact_sheet_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('project_fact_sheet_url', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('website_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('article_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('article_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('project_objectives', self.gf('django.db.models.fields.TextField')()),
            ('video_embed_code', self.gf('django.db.models.fields.TextField')()),
            ('video_title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('video_description', self.gf('django.db.models.fields.TextField')()),
            ('access_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.AccessType'], null=True, blank=True)),
            ('research_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.ResearchCategory'], null=True, blank=True)),
        ))
        db.send_create_signal('projects', ['Project'])

        # Adding model 'Presentation'
        db.create_table('projects_presentation', (
            ('file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['files.File'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_presentation_related', to=orm['projects.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('presentation_dt', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('projects', ['Presentation'])

        # Adding model 'Report'
        db.create_table('projects_report', (
            ('file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['files.File'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_report_related', to=orm['projects.Project'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('other', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('report_dt', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('projects', ['Report'])

        # Adding model 'Article'
        db.create_table('projects_article', (
            ('file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['files.File'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_article_related', to=orm['projects.Project'])),
            ('article_dt', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('projects', ['Article'])

        # Adding model 'Picture'
        db.create_table('projects_picture', (
            ('file_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['files.File'], unique=True, primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_picture_related', to=orm['projects.Project'])),
        ))
        db.send_create_signal('projects', ['Picture'])


    def backwards(self, orm):
        
        # Deleting model 'ProjectName'
        db.delete_table('projects_projectname')

        # Deleting model 'Program'
        db.delete_table('projects_program')

        # Deleting model 'ProgramYear'
        db.delete_table('projects_programyear')

        # Deleting model 'ProjectNumber'
        db.delete_table('projects_projectnumber')

        # Deleting model 'RpesaPm'
        db.delete_table('projects_rpesapm')

        # Deleting model 'AccessType'
        db.delete_table('projects_accesstype')

        # Deleting model 'ResearchCategory'
        db.delete_table('projects_researchcategory')

        # Deleting model 'Project'
        db.delete_table('projects_project')

        # Deleting model 'Presentation'
        db.delete_table('projects_presentation')

        # Deleting model 'Report'
        db.delete_table('projects_report')

        # Deleting model 'Article'
        db.delete_table('projects_article')

        # Deleting model 'Picture'
        db.delete_table('projects_picture')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'entities.entity': {
            'Meta': {'object_name': 'Entity'},
            'admin_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_creator'", 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'entity_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'entity_parent_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entity_type': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entity_owner'", 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'})
        },
        'files.file': {
            'Meta': {'object_name': 'File'},
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_creator'", 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '260'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'file_owner'", 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'perms.objectpermission': {
            'Meta': {'object_name': 'ObjectPermission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_groups.Group']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'projects.accesstype': {
            'Meta': {'object_name': 'AccessType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.article': {
            'Meta': {'object_name': 'Article', '_ormbases': ['files.File']},
            'article_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['files.File']", 'unique': 'True', 'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_article_related'", 'to': "orm['projects.Project']"})
        },
        'projects.picture': {
            'Meta': {'object_name': 'Picture', '_ormbases': ['files.File']},
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['files.File']", 'unique': 'True', 'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_picture_related'", 'to': "orm['projects.Project']"})
        },
        'projects.presentation': {
            'Meta': {'object_name': 'Presentation', '_ormbases': ['files.File']},
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['files.File']", 'unique': 'True', 'primary_key': 'True'}),
            'presentation_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_presentation_related'", 'to': "orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.program': {
            'Meta': {'object_name': 'Program'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.programyear': {
            'Meta': {'object_name': 'ProgramYear'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'access_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.AccessType']", 'null': 'True', 'blank': 'True'}),
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'article_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'article_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_creator'", 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'end_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_owner'", 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'participants': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_investigator': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_investigator_company': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'program_year': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProgramYear']", 'null': 'True', 'blank': 'True'}),
            'project_abstract': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'project_abstract_date': ('django.db.models.fields.DateTimeField', [], {}),
            'project_fact_sheet_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_fact_sheet_url': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectName']", 'null': 'True', 'blank': 'True'}),
            'project_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ProjectNumber']", 'null': 'True', 'blank': 'True'}),
            'project_objectives': ('django.db.models.fields.TextField', [], {}),
            'project_status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'research_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.ResearchCategory']", 'null': 'True', 'blank': 'True'}),
            'rpsea_pm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.RpesaPm']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "u''", 'unique': 'True', 'max_length': '200', 'db_index': 'True'}),
            'start_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'tags': ('tagging.fields.TagField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'video_description': ('django.db.models.fields.TextField', [], {}),
            'video_embed_code': ('django.db.models.fields.TextField', [], {}),
            'video_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website_title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'website_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'projects.projectname': {
            'Meta': {'object_name': 'ProjectName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.projectnumber': {
            'Meta': {'object_name': 'ProjectNumber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.report': {
            'Meta': {'object_name': 'Report', '_ormbases': ['files.File']},
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['files.File']", 'unique': 'True', 'primary_key': 'True'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_report_related'", 'to': "orm['projects.Project']"}),
            'report_dt': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.researchcategory': {
            'Meta': {'object_name': 'ResearchCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'projects.rpesapm': {
            'Meta': {'object_name': 'RpesaPm'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'user_groups.group': {
            'Meta': {'object_name': 'Group'},
            'allow_anonymous_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_anonymous_view': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_member_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_member_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_self_add': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_self_remove': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_user_edit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_user_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_respond': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'auto_respond_priority': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'auto_respond_template': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_creator'", 'to': "orm['auth.User']"}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_recipient': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['entities.Entity']", 'null': 'True', 'blank': 'True'}),
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['user_groups.GroupMembership']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_owner'", 'to': "orm['auth.User']"}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'group_permissions'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'show_as_option': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('tendenci.core.base.fields.SlugField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'distribution'", 'max_length': '75', 'blank': 'True'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'user_groups.groupmembership': {
            'Meta': {'unique_together': "(('group', 'member'),)", 'object_name': 'GroupMembership'},
            'create_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'creator_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_groups.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'group_member'", 'to': "orm['auth.User']"}),
            'owner_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'owner_username': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'status_detail': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '50'}),
            'update_dt': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']
