This is a script that reads stdin line by line and computes metrics:

<ul>
	<li> Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
	<li> After every 10 lines and/or a keyboard interruption , prints the statistics from the beginning:
</ul>

The number of possible status codes are <em>200</em> <em>301</em> <em>400</em> <em>401</em> <em>403</em> <em>404</em> <em>405</em> <em>500</em>

The status codes are printed in ascending order
