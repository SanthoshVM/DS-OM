function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.getElementById("closeNav").style.display = 'inline-block';
    document.getElementById("openNav").style.display = 'none';
}
function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.getElementById("openNav").style.display = 'inline-block';
    document.getElementById("closeNav").style.display = 'none';
}

checked=false;
function checkedAll_1 (frm1) {var aa= document.getElementById('frm1'); if (checked == false)
{
checked = true
}
else
{
checked = false
}for (var i =0; i < aa.elements.length; i++){ aa.elements[i].checked = checked;}
}
checked=false;
function checkedAll_2 (frm2) {var aa= document.getElementById('frm2'); if (checked == false)
{
checked = true
}
else
{
checked = false
}for (var i =0; i < aa.elements.length; i++){ aa.elements[i].checked = checked;}
}
function f1(){
  alert("Mining will start in new tab, which can be closed. To view status of mining click on VIEW MINING STATUS button.");
}
function f2(){
 if(flag==1)
 {
   document.getElementById("create_recipe").style.display='inline-block';
   document.getElementById("test_recipe").style.display='none';
 }
}
