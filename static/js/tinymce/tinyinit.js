tinymce.init({
    selector: "textarea",
    statusbar: false,
  
  	width: '100%',
  	height: 400,
  	autoresize_min_height: 400,
  	autoresize_max_height: 800,


// ===========================================
// INCLUDE THE PLUGIN
// ===========================================


	
plugins: [
    "advlist autolink lists link image charmap print preview anchor",
    "searchreplace visualblocks code fullscreen",
    "insertdatetime media table contextmenu paste autoresize"
],
	
// ===========================================
// PUT PLUGIN'S BUTTON on the toolbar
// ===========================================
	
toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image preview",
	
// ===========================================
// SET RELATIVE_URLS to FALSE (This is required for images to display properly)
// ===========================================
	
relative_urls: false

	
});


