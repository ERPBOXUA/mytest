###################################################################################
#
#    Copyright (C) 2020 Cetmix OÜ
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU LESSER GENERAL PUBLIC LICENSE as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

from odoo import _

IMAGE_PLACEHOLDER = "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"  # noqa

# Number of symbols to show as a message preview in TreeView
DEFAULT_MESSAGE_PREVIEW_LENGTH = 200

# Used to render dates in html TreeView
MONTHS = {
    1: _("Jan"),
    2: _("Feb"),
    3: _("Mar"),
    4: _("Apr"),
    5: _("May"),
    6: _("Jun"),
    7: _("Jul"),
    8: _("Aug"),
    9: _("Sep"),
    10: _("Oct"),
    11: _("Nov"),
    12: _("Dec"),
}

# Used to render html field in TreeView
TREE_TEMPLATE = (
    '<table style="width:100%%;border:none;%(background_color)s" title="%(title)s">'
    "<tbody>"
    "<tr>"
    '<td style="width: 1%%;"><img class="rounded-circle"'
    ' style="width: 64px; padding:10px;" src="data:image/png;base64,%(avatar)s"'
    ' alt="Avatar" title="%(author_display)s" width="100" border="0" /></td>'
    '<td style="width: 99%%;">'
    '<table style="width: 100%%; border: none;">'
    "<tbody>"
    "<tr>"
    '<td id="author"><strong>%(author_display)s</strong> &nbsp; '
    '<span id="subject">%(subject)s</span></td>'
    '<td id="date" style="text-align:right;">'
    '<span title="%(message_date)s" id="date">%(date_display)s</span></td>'
    "</tr>"
    "<tr>"
    "<td>"
    '<p id="related-record" style="font-size: x-small;">'
    "<strong>%(record_ref)s</strong></p></td>"
    '<td id="notifications" style="text-align: right;">%(icons)s</td>'
    "</tr>"
    "</tbody>"
    "</table>"
    "<b id='daleted-days' class='text-danger'>"
    "%(display_number_days_after_deletion)s"
    "</b>"
    '<p id="text-preview" style="color: #808080;">%(body)s</p>'
    "</td>"
    "</tr>"
    "</tbody>"
    "</table>"
)

BLOCK_QUOTE = (
    "<p><br/></p>"
    "<br/>"
    "<blockquote>----- Original message ----- <br/> Date: %(date)s <br/>"
    " From: %(author)s <br/> Subject: %(subject)s <br/><br/>%(body)s</blockquote>"
)

# Used to render html field in TreeView
CONVERSATION_TREE_TEMPLATE = (
    '<table style="width: 100%%; border: none;" title="Conversation">'
    "<tbody>"
    "<tr>"
    '<td style="width: 1%%;"><img class="rounded-circle" '
    'style="height: auto; width: 64px; padding:10px;"'
    ' src="data:image/png;base64, %(avatar)s" alt="Avatar" '
    'title="%(title)s" width="100" border="0" /></td>'
    '<td style="width: 99%%;">'
    '<table style="width: 100%%; border: none;">'
    "<tbody>"
    "<tr>"
    '<td id="author"><strong>%(author)s</strong> &nbsp; '
    '<span id="subject">%(subject)s</span></td>'
    '<td id="date" style="text-align: right;" title="%(date)s">%(date_display)s</td>'
    "</tr>"
    "<tr>"
    '<td><p id="notifications" style="font-size: x-small;">'
    "<strong>%(msg_count_text)s</strong></p></td>"
    '<td id="participants" style="text-align: right;">%(participant)s</td>'
    "</tr>"
    "</tbody>"
    "</table>"
    "%(body)s"
    "</td>"
    "</tr>"
    "</tbody>"
    "</table>"
)

PARTICIPANT_IMG = (
    '<img class="rounded-circle"'
    ' style="width:24px;max-height:24px;margin:2px;"'
    ' title="%(title)s" src="data:image/png;base64, %(img)s"/>'
)

PLAIN_BODY = (
    '<img class="rounded-circle"'
    ' style="width:16px;max-height:16px;margin:2px;"'
    ' title="%(title)s" src="data:image/png;base64, %(img)s"/>'
    ' <span id="text-preview"'
    ' style="color:#808080;vertical-align:middle;">%(body)s</p>'
)

DEFAULT_SIGNATURE_LOCATION = "a"
