#!/usr/bin/env python
import tba_config
import webapp2

from controllers.apiv3 import api_status_controller as asc
from controllers.apiv3 import api_district_controller as adc
from controllers.apiv3 import api_event_controller as aec
from controllers.apiv3 import api_match_controller as amc
from controllers.apiv3 import api_team_controller as atc

# Ensure that APIv3 routes include OPTIONS method for CORS preflight compatibility
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests
app = webapp2.WSGIApplication([
    # Overall status
    webapp2.Route(r'/api/v3/status',
        asc.ApiStatusController, methods=['GET', 'OPTIONS']),
    # Team List
    webapp2.Route(r'/api/v3/teams/<page_num:([0-9]+)>',
        atc.ApiTeamListController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<page_num:([0-9]+)>/<model_type:(simple|keys)>',
        atc.ApiTeamListController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<year:([0-9]+)>/<page_num:([0-9]+)>',
        atc.ApiTeamListController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/teams/<year:([0-9]+)>/<page_num:([0-9]+)>/<model_type:(simple|keys)>',
        atc.ApiTeamListController, methods=['GET', 'OPTIONS']),
    # Team
    webapp2.Route(r'/api/v3/team/<team_key:>',
        atc.ApiTeamController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/<model_type:(simple)>',
        atc.ApiTeamController, methods=['GET', 'OPTIONS']),
    # Team History
    webapp2.Route(r'/api/v3/team/<team_key:>/years_participated',
        atc.ApiTeamYearsParticipatedController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/districts',
        atc.ApiTeamHistoryDistrictsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/robots',
        atc.ApiTeamHistoryRobotsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/social_media',
        atc.ApiTeamSocialMediaController, methods=['GET', 'OPTIONS']),
    # Team Events
    webapp2.Route(r'/api/v3/team/<team_key:>/events',
        atc.ApiTeamEventsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<model_type:(simple|keys)>',
        atc.ApiTeamEventsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<year:([0-9]+)>',
        atc.ApiTeamEventsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/events/<year:([0-9]+)>/<model_type:(simple|keys)>',
        atc.ApiTeamEventsController, methods=['GET', 'OPTIONS']),
    # Team @ Event
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/matches',
        atc.ApiTeamEventMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/matches/<model_type:(simple|keys)>',
        atc.ApiTeamEventMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/awards',
        atc.ApiTeamEventAwardsController, methods=['GET', 'OPTIONS']),
    # webapp2.Route(r'/api/v3/team/<team_key:>/event/<event_key:>/status',
    #     ApiStatusController, methods=['GET', 'OPTIONS']),
    # Team Awards
    webapp2.Route(r'/api/v3/team/<team_key:>/awards',
        atc.ApiTeamHistoryAwardsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/awards/<year:([0-9]+)>',
        atc.ApiTeamYearAwardsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/matches/<year:([0-9]+)>',
        atc.ApiTeamYearMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/matches/<year:([0-9]+)>/<model_type:(simple|keys)>',
        atc.ApiTeamYearMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/team/<team_key:>/media/<year:([0-9]+)>',
        atc.ApiTeamYearMediaController, methods=['GET', 'OPTIONS']),
    # Event List
    webapp2.Route(r'/api/v3/events/<year:([0-9]+)>',
        aec.ApiEventListController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/events/<year:([0-9]+)>/<model_type:(simple|keys)>',
        aec.ApiEventListController, methods=['GET', 'OPTIONS']),
    # Event
    webapp2.Route(r'/api/v3/event/<event_key:>',
        aec.ApiEventController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/<model_type:(simple)>',
        aec.ApiEventController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/<detail_type:(alliances|district_points|rankings|stats)>',
        aec.ApiEventDetailsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/teams',
        aec.ApiEventTeamsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/teams/<model_type:(simple|keys)>',
        aec.ApiEventTeamsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/matches',
        aec.ApiEventMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/matches/<model_type:(simple|keys)>',
        aec.ApiEventMatchesController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/event/<event_key:>/awards',
        aec.ApiEventAwardsController, methods=['GET', 'OPTIONS']),
    # Match
    webapp2.Route(r'/api/v3/match/<match_key:>',
        amc.ApiMatchController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/match/<match_key:>/<model_type:(simple)>',
        amc.ApiMatchController, methods=['GET', 'OPTIONS']),
    # District List
    webapp2.Route(r'/api/v3/districts/<year:([0-9]+)>',
        adc.ApiDistrictListController, methods=['GET', 'OPTIONS']),
    # District
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/events',
        adc.ApiDistrictEventsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/events/<model_type:(simple|keys)>',
        adc.ApiDistrictEventsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/teams',
        adc.ApiDistrictTeamsController, methods=['GET', 'OPTIONS']),
    webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/teams/<model_type:(simple|keys)>',
        adc.ApiDistrictTeamsController, methods=['GET', 'OPTIONS']),
    # webapp2.Route(r'/api/v3/district/<district_key:>/<year:([0-9]+)>/rankings',
    #     ApiStatusController, methods=['GET', 'OPTIONS']),
], debug=tba_config.DEBUG)
