$(function () {

    flag1 = false;//表示 用户名   输入是否合法
    flag2 = false;//表示 密码     输入是否合法
    flag3 = false;//表示 确认密码  输入是否合法
    flag4 = false;//表示 邮箱     输入是否合法

    // //用户名
    // $('#username').change(function () {
    //     var v = $(this).val();
    //     // 检测 v 是否满足 正则 条件
    //     if (/^[a-zA-z_]\w{5,17}$/.test(v)){
    //         // console.log('输入合法！')
    //         flag1 = true
    //     }
    //     else{
    //         // console.log('输入有误/！')
    //         flag1 = false
    //     }
    // });

     //用户名
    $('#username').change(function () {
        var v = $(this).val();
        // 检测 v 是否满足 正则 条件
        if (/^[a-zA-z_]\w{5,17}$/.test(v)){
            flag1 = true
            //如果输入格式正确,则验证用户名是否存在
            $.get('/app/checkusername/',{username:$(this).val()},function (data) {
                // console.log(data)
                if ( data.status == 1){
                    $('#msg').html('用户名可以使用').css('color','green')
                }
                else if (data['status'] == 0) {
                    $('#msg').html(data.msg).css('color','red')
                }
                else{
                    $('#msg').html('用户名不合法').css('color','red')
                }
            })
        }
        else{
            flag1 = false
            $('#msg').html('用户名输入不正确').css('color','red')

        }
    });



    //密码
    $('#password').change(function () {
        var v = $(this).val();
        // 检测 v 是否满足 正则 条件
        if (/^.\w{8,}$/.test(v)){
            console.log('密码输入合法！')
             flag2 = true
        }
        else{
            console.log('密码输入有误！')
            flag2 = false
        }
    });
     //确认密码
    $('#again').change(function () {
        var v =$(this).val();
        if ( v == $('#password').val()){
            console.log('输入合法！')
            flag3 = true
        }
        else{
            console.log('输入有误！')
            flag3 = false
        }
    });
    //邮箱
    $('#email').change(function () {
        var v = $(this).val();
        // 检测 v 是否满足 正则 条件
        if (/^\w+@\w+\.\w+$/.test(v)){
            console.log('输入合法！')
            flag4 = true
        }
        else{
            console.log('输入有误！')
            flag4 = false
        }
    });

    // 注册
    $('#register').click(function () {

        if (flag1 && flag2 && flag3  && flag4 ){

            alert('注册成功')
            //表单提交md5加密后的密码
            $('#password').val(md5($('#password').val()))
            return true
        }
        else{
            alert('输入有误')
            return false //阻止按键提交
        }
    })


    //检测用户名是否存在
    //jq里面有事件监听器,是可以同时存在的
    // $('#username').change(function () {
    //
    //
    //     // JQ 中的Ajax
    //     /*
    //     $.ajax({
    //         type:'get', // 默认是get 可以不写
    //         url: '',    //请求的路径,必须写
    //         data:{},    // 提交参数
    //         async:true, //ajax请求,可以不写,默认是true,异步的意思
    //
    //         //请求成功返回的函数(回调函数)
    //         success:function (data) {
    //             console.log(data)
    //         },
    //         //请求失败的回调函数
    //         error:function (err) {
    //             console.log(err)
    //         }
    //     })
    //     */
    //
    //     /*
    //     //两个的使用方法一样的
    //     $.get('url',{},function (data) {
    //
    //     })
    //     $.post('url',{},function (data) {
    //
    //     })
    //     $.getJSON('url',{},function (data) {
    //
    //     })
    //     */
    //
    //     $.get('/app/checkusername/',{username:$(this).val()},function (data) {
    //         // console.log(data)
    //         if ( data.status == 1){
    //             $('#msg').html('用户名可以使用').css('color','green')
    //         }
    //         else if (data['status'] == 0) {
    //             $('#msg').html(data.msg).css('color','red')
    //         }
    //         else{
    //             $('#msg').html('用户名不合法').css('color','red')
    //
    //         }
    //     })
    //
    //
    //
    //
    // })


})