from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ViewSet, GenericViewSet

from API.models import Book
from day4.serializer import BookModelSerializer
from utils.response import APIResponse


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_objects_all = Book.objects.all()
        serializer = BookModelSerializer(book_objects_all, many=True).data
        return APIResponse(results=serializer)
class BookGenericAPIView(ListModelMixin,
                         RetrieveModelMixin,
                         CreateModelMixin,
                         DestroyModelMixin,
                         UpdateModelMixin,
                         GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = "id"
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:

            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # 局部修改
    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(results=response.data)
class BookGenericAPIViewV2(ListAPIView):
    queryset = Book.objects.filter(is_delete=False)
    serializer_class = BookModelSerializer
class UserAPIView(ViewSet):

    def user_login(self, request, *args, **kwargs):
        return APIResponse("登录成功")
    def get_user_count(self, request, *args, **kwargs):

        print("查询完成")
        return APIResponse("查询完成")
class UserGenericViewSet(GenericViewSet, ListModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def user_list(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
