from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(_("Firstname"), max_length=100)
    last_name = models.CharField(_("Lastname"), max_length=100)
    email_address = models.EmailField(_("E-mail"), max_length=254)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    excerpt = models.CharField(_("Excerpt"), max_length=254)
    image_name = models.CharField(_("Image Name"), max_length=100)
    date = models.DateField(_("Date"), auto_now=True)
    # We don't really need to set an index for slugs
    # since the slugfield already is indexed and, in any case,
    # unique true sets it like that automatically
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    content = models.TextField(_("Content"), validators=[
                               MinLengthValidator(10)])
    # we add a related name to let us query posts from authors with just .posts
    # instead of author.post_set
    author = models.ForeignKey("blog.Author",
                               verbose_name=_("Author"), null=True,
                               on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField("blog.Tag", verbose_name=_("Tag"))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    caption = models.CharField(_("Tag"), max_length=20)

    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})
