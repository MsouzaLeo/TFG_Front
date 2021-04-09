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

/*Export dos dados da Table em CSV*/
var name_file = document.getElementById('name').innerHTML;
var options = {
    'separator': ";",
    'filename': name_file + ".csv"
}
$('#downloadcsv').on('click', function() {
    $('#table').table2csv(options);
});