#!/usr/bin/env python
import tba_config
import webapp2

from controllers.apiv3.api_status_controller import ApiStatusController
from controllers.apiv3.api_team_controller import ApiTeamListController

# Ensure that APIv3 routes include OPTIONS method for CORS preflight compatibility
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests
app = webapp2.WSGIApplication([
    # Overall status
    webapp2.Route(r'/api/v3/status',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # Team List
    webapp2.Route(r'/api/v3/teams/<page_num:([0-9]+)>',
        ApiTeamListController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<page_num:([0-9]+)>/<type:(simple|keys)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<year:([0-9]+)>/<page_num:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<year:([0-9]+)>/<page_num:([0-9]+)>/<type:(simple|keys)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # Team
    webapp2.Route(r'/api/v3/team/<team_key:>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/simple',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/years_participated',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/districts',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/robots',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<type:(simple|keys)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<year:([0-9]+)>/<type:(simple|keys)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/matches/<match_type:>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/matches/<match_type:>/<type:(simple|keys)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/awards',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/status',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/awards',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/awards/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/matches/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/matches/<year:([0-9]+)>/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/media/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/social_media',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # Event List
    webapp2.Route(r'/api/v3/events/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/events/<year:([0-9]+)>/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # Event
    webapp2.Route(r'/api/v3/event/<event_key:>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/elim_alliances',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/stats',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/rankings',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/district_points',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/teams',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/teams/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/matches',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/matches/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/awards',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # Match
    webapp2.Route(r'/api/v3/match/<match_key:>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/match/<match_key:>/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # District List
    webapp2.Route(r'/api/v3/districts/<year:([0-9]+)>',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    # District
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/events',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/events/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/teams',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/teams/<type:(simple|keys)',
        ApiStatusController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/rankings',
        ApiStatusController, methods=['GET', 'OPTIONS']),
], debug=tba_config.DEBUG)