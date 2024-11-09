document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});

function closeAllLists(el=null) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    let autocompletes = document.querySelectorAll(".autocomplete-items");
    if (el) {
        for (let i = 0; i < autocompletes.length; i++) {
            if (el != autocompletes[i]) {
            autocompletes[i].parentNode.removeChild(autocompletes[i]);
          }
        }
    } else {
        autocompletes.forEach((item) => item.parentNode.removeChild(item));
    }
}


htmx.on("htmx:afterSwap", (e) => {
    console.log("htmx:afterSwap", e)
    const dispatchEl = e.detail.elt
    console.log(dispatchEl, dispatchEl.parentElement);
    if (dispatchEl.classList.contains('autocomplete')) {
        const autocompleteItems = document.querySelectorAll('.autocomplete-items .item')
        console.log(autocompleteItems);
        autocompleteItems.forEach((item) => {
            item.addEventListener('click', (e) => {
                const inp = e.target.closest('.autocomplete').querySelector('input');
                inp.value = e.target.querySelector('input').value;
                console.log(inp, inp.value, e.target.querySelector('input'), e.target.querySelector('input').value);
                closeAllLists()
            })
        })
    }
})