sqlite> create table Slides (id  text, title text);
sqlite> create table Refs (id text, type text, slide_id text, foreign key(slide_id) references Slides(id));
sqlite> create table Slide_xref (id text, slide_id text, referenced text, foreign key(slide_id) references Slides(id));
sqlite> insert into Slides VALUES('slide000', 'abc');
sqlite> insert into Refs values ('1', 'url', 'slide000');
sqlite> insert into Refs values ('2', 'web', 'slide000');
sqlite> insert into Slide_xref values('1', 'slide000', 'slide001');
sqlite> select * from Slides s JOIN Refs r on s.id = r.slide_id
   ...> JOIN Slide_xref x on s.id = x.slide_id;
slide000|abc|1|url|slide000|1|slide000|slide001
slide000|abc|2|web|slide000|1|slide000|slide001
sqlite> insert into Slide_xref values('2', 'slide000', 'slide002');
sqlite> select * from Slides s JOIN Refs r on s.id = r.slide_id
   ...> JOIN Slide_xref x on s.id = x.slide_id;
slide000|abc|1|url|slide000|1|slide000|slide001
slide000|abc|1|url|slide000|2|slide000|slide002
slide000|abc|2|web|slide000|1|slide000|slide001
slide000|abc|2|web|slide000|2|slide000|slide002
