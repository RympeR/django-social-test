"""
    @api {POST} /api/social/user/signup/  Sign up
    @apiName Sign up
    @apiGroup User
    @apiDescription Sign up
    
    @apiParam {String} name User name
    @apiParam {String} login User unique login
    @apiParam {String} password User password

    @apiSuccess {Number} like Id of created user
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1
    }
"""
"""
    @api {POST} /api/social/user/login/ Log in
    @apiName Log in
    @apiGroup User
    @apiDescription Log in

    @apiParam {String} login User unique login
    @apiParam {String} password User password

    @apiSuccess {Number} like Id of got user
    @apiSuccess {String} auth_token Now it is just test
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "auth_token": 'test'
    }
"""
"""
    @api {POST} /api/social/user/get-profile/{pk} Get profile
    @apiName Get profile
    @apiGroup User
    @apiDescription Get profile

    @apiParam {Number} pk User id

    @apiSuccess {Number} id Id of got user
    @apiSuccess {String} name user name
    @apiSuccess {String} login user login
    @apiSuccess {String} password user password
    @apiSuccess {String} last_login last login time
    @apiSuccess {String} last_request last request time
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "id": 1,
        "name": "test",
        "login": "test1",
        "password": "test-pass",
        "last_login": "08:41:36.374845",
        "last_request": "15:17:23.433469"
    }
"""