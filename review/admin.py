from django.contrib import admin
from review.models import Review, Product

# 관리자 화면에서 부모 객체를 보여줄 때 자식을 함께 보여주기 위한 클래스 작성
# Album:Photo = 부모:자식 관계이므로, 앨범 출력할 때 사진을 함께 보여줄 수 있음
# 출력 형식은 StackedInline(세로 나열형) 및 TabularInline(가로 나열형) 두 종류
class ReviewInline(admin.StackedInline):
    model = Review               # 추가로 함께 출력할 자식 테이블을 지정
    extra = 2                   # 함께 등록할 Review 테이블의 객체 수 지정

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]     # 상품 객체와 동시에 처리할 자식 클래스 지정
    list_display = ('name', 'description')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date')

admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
