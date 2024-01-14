(function () {
    "use strict";
    /*---------------------------------------------------------------------
        Fieldset
    -----------------------------------------------------------------------*/
    
    let currentTab =0;
    const ActiveTab=(n)=>{
        if(n==0){
            document.getElementById("datadiri").classList.add("active");
            document.getElementById("datadiri").classList.remove("done");
            document.getElementById("ortu").classList.remove("done");
            document.getElementById("ortu").classList.remove("active");
        }
        if(n==1){
            document.getElementById("datadiri").classList.add("done");
            document.getElementById("ortu").classList.add("active");
            document.getElementById("ortu").classList.remove("done");
            document.getElementById("wali").classList.remove("active");
            document.getElementById("wali").classList.remove("done");
            document.getElementById("berkas").classList.remove("done");
            document.getElementById("berkas").classList.remove("active");

        }
        if(n==2){
            document.getElementById("datadiri").classList.add("done");
            document.getElementById("ortu").classList.add("done");
            document.getElementById("wali").classList.add("active");
            document.getElementById("wali").classList.remove("done");
            document.getElementById("berkas").classList.remove("done");
            document.getElementById("berkas").classList.remove("active");
        }
        if(n==3){
            document.getElementById("datadiri").classList.add("done");
            document.getElementById("ortu").classList.add("done");
            document.getElementById("wali").classList.add("done");
            document.getElementById("berkas").classList.add("active");
            document.getElementById("berkas").classList.add("done");
        }
    } 
    const showTab=(n)=>{
        var x = document.getElementsByTagName("fieldset");
        x[n].style.display = "block";
        console.log(n);
        ActiveTab(n);
       
    }
    const nextBtnFunction= (n) => {
        var x = document.getElementsByTagName("fieldset");
        x[currentTab].style.display = "none";
        currentTab = currentTab + n;
        showTab(currentTab);
    }
    
    const nextbtn= document.querySelectorAll('.next')
    Array.from(nextbtn, (nbtn) => {
    nbtn.addEventListener('click',function()
    {
        nextBtnFunction(1);
    })
});

// previousbutton

const prebtn= document.querySelectorAll('.previous')
    Array.from(prebtn, (pbtn) => {
    pbtn.addEventListener('click',function()
    {
        nextBtnFunction(-1);
    })
});
    
})()