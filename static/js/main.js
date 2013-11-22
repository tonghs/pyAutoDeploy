/**
 * Created by Administrator on 13-11-18.
 */
$(document).ready(function(){
//
//    $('#btn').click(function(){
//        var data = {'payload': '{"ref":"refs/heads/master","after":"600efaa41de9b4a32196ca602ae429a053aff2d2","before":"9e691fda5c93b10a1c2dd08e330aaa9a0e406a56","created":false,"deleted":false,"forced":false,"compare":"https://github.com/tonghuashuai/pyAutoDeploy/compare/9e691fda5c93...600efaa41de9","commits":[{"id":"600efaa41de9b4a32196ca602ae429a053aff2d2","distinct":true,"message":"test","timestamp":"2013-11-18T05:45:17-08:00","url":"https://github.com/tonghuashuai/pyAutoDeploy/commit/600efaa41de9b4a32196ca602ae429a053aff2d2","author":{"name":"tonghs","email":"tonghuashuai@126.com","username":"tonghuashuai"},"committer":{"name":"tonghs","email":"tonghuashuai@126.com","username":"tonghuashuai"},"added":[],"removed":[],"modified":["main.py"]}],"head_commit":{"id":"600efaa41de9b4a32196ca602ae429a053aff2d2","distinct":true,"message":"test","timestamp":"2013-11-18T05:45:17-08:00","url":"https://github.com/tonghuashuai/pyAutoDeploy/commit/600efaa41de9b4a32196ca602ae429a053aff2d2","author":{"name":"tonghs","email":"tonghuashuai@126.com","username":"tonghuashuai"},"committer":{"name":"tonghs","email":"tonghuashuai@126.com","username":"tonghuashuai"},"added":[],"removed":[],"modified":["main.py"]},"repository":{"id":14487342,"name":"pyAutoDeploy","url":"https://github.com/tonghuashuai/pyAutoDeploy","description":"\u81ea\u52a8\u90e8\u7f72\u5de5\u5177","watchers":0,"stargazers":0,"forks":0,"fork":false,"size":284,"owner":{"name":"tonghuashuai","email":"tonghuashuai@126.com"},"private":false,"open_issues":0,"has_issues":true,"has_downloads":true,"has_wiki":true,"language":"Python","created_at":1384765483,"pushed_at":1384782338,"master_branch":"master"},"pusher":{"name":"tonghuashuai","email":"tonghuashuai@126.com"}}'};
//        $.post('/push', data, function(data){
//        });
//    });
    resize();
    $(window).resize(resize);
});

function resize(){
    $('.main').css('min-height', $(window).height() - 100)
    $('.left').css('min-height', $('.main').height() - 10);
}

function del(id, obj){
    $.post('/del', {'id': id}, function(data){
        if (data == 'success'){
            obj.parent().parent().fadeOut();
        }
    });
}

function execute(id, obj){
    obj.parent().parent().children('.state').attr('class', 'state');
    obj.parent().parent().children('.state').html('执行中');
    $.post('/execute', {'id': id}, function(data){
        if (data != null && data != ''){
            data = $.parseJSON(data);
            obj.parent().parent().children('.state').html(data.msg);
            obj.parent().parent().children('.exe_time').html(data.exe_time);
            obj.parent().parent().children('.state').attr('class', 'state state' + data.state);

        }
    }).error(function(){

        });
}