//向服务器post
  $("#sm").bind("click", function () {
    if ($("#password").val()) {
        $("#sm").button('loading');
        $.post("/signup", {username:$("#username").val(),password:$("#password").val()},
            function (data) {
              alert(data);
              if (data == '注册成功') {
                window.location.href = "/";
              }
          });
      } else {
        alert("用户名/密码不能为空呀");
      }
      $("#sm").button('reset');
    })