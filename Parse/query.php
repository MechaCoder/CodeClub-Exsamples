<html>
	<head>
		<?php include 'ImportFile.php';	?>
		<title></title>
	</head>
	<body>
		<script type="text/javascript">
			function conTest(){
				var TestObject = Parse.Object.extend("TestObject");
				var testObject = new TestObject();
				testObject.save({foo: "bar"}).then(function(Object) {alert('it worked');})}
			function consoleMapper():

		</script>
		<script type="text/javascript">
			var q = new	Parse.Query(Parse.Object.extend("Blog"));
			//var table = Parse.Object.extend("Blog");
			//var q = new Parse.Query(table); 
			q.equalTo('BlogTitle','TestTitle');
			q.find({
				success: function(results){
					//alert('q.find-Success -:- found: ' + results.length + ' results');
					for (var i = 0; i < results.length; i++) {
						var Object = results[i];
						console.log(Object.id);
						console.log(Object.get('BlogTitle'));
						console.log(Object.get('BlogContent'));
						console.log(Object.createdAt);
						console.log(Object.updatedAt);
					}},
				error: function(error){console.log("Error: " + error.code + " " + error.message);}
			});
		</script>
	</body>
</html>