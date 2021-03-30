var searchBtn = $('#search-btn');
var searchForm = $('#search-form');
var uploadBtn = $('#upload-btn');
var uploadForm = $('#upload-form');

$(searchBtn).on('click', function() {
    searchForm.submit();
})

$(uploadBtn).on('click', function() {
    uploadForm.submit();
})