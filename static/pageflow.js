$('.navbar .home').click(function(){
    $('.container').hide();
    $('.home-container').show();

    $('.nav-item').removeClass('active');
    $('.nav-item.home').addClass('active');
});

$('.navbar .help').click(function(){
    $('.container').hide();
    $('.help-container').show();

    $('.nav-item').removeClass('active');
    $('.nav-item.help').addClass('active');
});

$('.navbar .record').click(function(){
    $('.container').hide();
    $('.record-container').show();

    $('.nav-item').removeClass('active');
    $('.nav-item.record').addClass('active');
});

$('.navbar .transcripts').click(function(){
    $('.container').hide();
    $('.transcript-table-container').show();

    $('.nav-item').removeClass('active');
    $('.nav-item.transcripts').addClass('active');
});

$('#cancelUpload').click(function(){
    $('#recordingsList').hide();
    $('#upload-complete-container').hide();
});