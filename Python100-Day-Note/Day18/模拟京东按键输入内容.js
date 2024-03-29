/*
当我们按下s键，光标就定位到搜索框

案例分析：核心思路︰

①检测用户是否按下了s键，如果按下s键，就把光标定位到搜索框里面

②使用键盘事件对象里面的keyCode判断用户按下的是否是s键

③搜索框获得焦点:使用js 里面的focus()方法

*/
var search = document.querySelector('input');
document.addEventListener('keyup', function (e) {
    // console.log(e.keyCode);
    if (e.keyCode === 83) {
        search.focus();
    }
})
