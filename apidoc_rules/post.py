"""
    @api {POST} /api/social/post/create/  Create post
    @apiName Create post
    @apiDescription Create post
    @apiGroup Post
    
    @apiParam {Number} user_id Id user
    @apiParam {String} name Post name

    @apiSuccess {Number} post Id of created post
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "post": 209
    }
"""

"""
    @api {GET} /api/social/post/{pk} Get post
    @apiName Get post
    @apiDescription Get post
    @apiGroup Post

    @apiParam {Number} pk Post id

    @apiSuccess {Number} id Id of created post
    @apiSuccess {String} name Post name
    @apiSuccess {String} image Link to post image file
    @apiSuccess {String} description Post description
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "name": "twet",
        "image": "http://127.0.0.1:8000/media/PHZ_0733.jpg",
        "description": ""
    }
"""