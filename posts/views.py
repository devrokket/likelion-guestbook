from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post
import json

@require_http_methods(["POST"])
def create_post(request):
    body = json.loads(request.body.decode('utf-8'))
		
    new_post = Post.objects.create(
        title = body['title'],
        writer = body['writer'],
        content = body['content']
    )
		
    new_post_json = {
        "id": new_post.id,
        "title": new_post.title,
        "writer": new_post.writer,
        "content": new_post.content,
        "created_at": new_post.created_at,
    }

    return JsonResponse({
        'status': 200,
        'message': '새 방명록 등록 완료',
        'data': new_post_json
    })

@require_http_methods(["GET"])
def get_post_all(request):
    post_all = Post.objects.all()

    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.id,
            "title": post.title,
            "writer": post.writer,
            "content": post.content,
            "created_at": post.created_at,
        }
        post_json_all(post_json)

@require_http_methods(["GET"])
def get_post_all(request):

		# Post 데이터베이스에 있는 모든 데이터를 불러와 queryset 형식으로 저장함
    post_all = Post.objects.all()
    
		# 각 데이터를 Json 형식으로 변환하여 리스트에 저장함
    post_json_all = []
    for post in post_all:
        post_json = {
            "id": post.id,
            "title": post.title,
            "writer": post.writer,
            "content": post.content,
            "created_at": post.created_at,
        }
        post_json_all.append(post_json)
    
    return JsonResponse({
        'status': 200,
        'message': '모든 방명록 조회 성공',
        'data': post_json_all
    })

@require_http_methods(["GET", "DELETE"])
def post_detail(request, id):
		# 요청 메소드가 GET일 때는 게시글을 조회하는 View가 동작하도록 함
    if request.method == "GET":
        post = get_object_or_404(Post, pk=id)
        
        post_json = {
            "id": post.id,
            "title": post.title,
            "writer": post.writer,
            "content": post.content,
            "created_at": post.created_at,
        }

        return JsonResponse({
            'status': 200,
            'message': '방명록 조회 성공',
            'data': post_json
        })
    elif request.method == "DELETE":
        delete_post = get_object_or_404(Post, pk=id)
        delete_post.delete()

        return JsonResponse({
                'status': 200,
                'message': '방명록 삭제 성공',
                'data': None
        })