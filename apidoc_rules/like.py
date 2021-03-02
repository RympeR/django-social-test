"""
    @api {POST} /api/social/like/create/ Create like
    @apiName Create like
    @apiGroup Like

    @apiParam {Number} post Post id
    @apiParam {Number} user User id
    @apiParam {Boolean} liked Is post liked or unliked?

    @apiSuccess {Number} like Id of created like
"""

"""
    @api {GET} /api/social/analytics/ Get like stats    
    @apiName Get like stats
    @apiGroup Like

    @apiParam begin_date Start range date
    @apiParam end_date End range date

    @apiSuccess {object} stats Grouped by date amount of likes
    @apiSuccessExample Success-Response:
    HTTP/1.1 200 OK
    {
        "stats": [
        {
            "added_date": "2021-03-01",
            "dcoun": 1
        },
        {
            "added_date": "2021-03-02",
            "dcoun": 196
        }
    ]
    }
"""