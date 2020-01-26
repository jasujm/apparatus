from unittest import TestCase
from unittest.mock import Mock

from apparatus import models, settings
from apparatus.templatetags import apparatus_tags


class BlogCommentTest(TestCase):
    def testRenderBlogComments(self):
        self.assertEqual(
            apparatus_tags.comment_section(
                {"meta": Mock(url="localhost"), "post": Mock(guid="guid"),}
            ),
            {
                "apparatus_site": settings.APPARATUS_DISQUS_SITE,
                "page_url": "localhost",
                "page_identifier": "guid",
            },
        )
