function deleteItem(itemId) {
   fetch("/delete-item", {
     method: "POST",
     body: JSON.stringify({ itemId: itemId }),
   }).then((_res) => {
     window.location.href = "/";
   });
 }

 function editItem(itemId) {
   const url = "edit-item?id=" + itemId
   window.location.href = url;
 }