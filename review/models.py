from django.db import models
# reverse() 함수는 URL 패턴을 만들어주는 장고 내장 함수
from django.core.urlresolvers import reverse
# ThumbnailImageField 클래스는 사진 원본 및 썸네일 이미지를 저장하는
# (fields.py 파일에서 정의할) 커스텀 필드
from review.fields import ThumbnailImageField
from pytz import timezone


class Product(models.Model):
	name = models.CharField('제품 이름', max_length=50)
	description = models.CharField('제품 내용', max_length=100, blank=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/album/99 형식의 값을 반환
		return reverse('review:product_detail', args=(self.id,))


class Review(models.Model):
	# 자신의 부모(Album)에 대한 외래키
	product = models.ForeignKey(Product)
	title = models.CharField('리뷰 제목', max_length=50)
	# ThumbnailImageField는 upload_to 옵션으로 저장 위치를 지정
	# MEDIA_ROOT로 지정된 폴더 하위에 /product/2018/03/과 같은 폴더를 생성하고,
	# 여기에 업로드된 파일을 자동적으로 저장해줌
	image = ThumbnailImageField(upload_to='review/%Y/%m')
	description = models.TextField('리뷰 설명', blank=True)
	# settings.TIME_ZONE = 'Asia/Seoul' 으로 설정해도 UTC 시각으로 처리됨
	# DB에 저장되는 시각은 UTC 시각이지만, 아래 속성 처리로 한국 시각으로 변환하여 템플릿에 제공함
	upload_date = models.DateTimeField('등록 일시', auto_now_add=True)

	# # 아래와 같이 속성 처리를 변경해야 한국 시각으로 처리됨
	# @property
	# def created_at_korean_time(self):
	# 	korean_timezone = timezone(settings.TIME_ZONE)
	# 	return self.created_at.astimezone(korean_timezone)

	class Meta:
		ordering = ['upload_date']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# 이 메소드가 정의된 객체의 URL /photo/photo/99 형식의 값을 반환
		return reverse('review:review_detail', args=(self.id,))