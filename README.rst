Kawaz 3rd Portal Websiteの開発場所です。暇がそんなに無いのでゆっくりやっていきます。
ひとまずの目標はDjango 1.3用に書き換えたコードで現状と同等の機能を持つまで開発を行うことです。


格言
=====================================

1.	面倒くさいけど真面目にテストコードを書こう
2.	面倒くさいけど真面目にドキュメントコメントを書こう
3.	面倒くさいけど分離可能なものは外部ライブラリとして分離しブラッシュアップしよう
	（その場合はドキュメントコメントなどはすべて英語化しGithubなどで公開できるレベルまで
	ブラッシュアップ）
4.	面倒くさいけどくじけないで頑張ろう


最終的に追加する予定の機能
======================================

-	``django-mfw``を用いた携帯・スマートフォン対応
-	``django-piston``を用いたKawaz APIの作成
-	``django-markupfield``を用いた複数フォーマット対応の入力欄
	（Markdown, Texlie, RestructuredText, HTMLなどのフォーマットを
	ユーザーが投稿時に自由にいじれるようにする。それに合わせてMarkItUpの
	スキンやセットを自動変更）
-	``Akismet``を用いたスパムコメントやスパム投稿の排除
-	Kawaz内宣伝システムの構築（現在ハードコーディングで行っている作業）
-	Kawaz内バージョン管理システム（Git, Mercurial, Subversionなど）
-	全体のUIデザインの見直し。不要なサイドバーをトグル可能もしくは排除
-	Kawaz Commonsの分離。素材と添付の違いを明確にする。


Python 関連資料
=====================================
Pythonの技能アップの為に以下に上げるコーディングスタイルガイドは必読

-	`Google Python Style Guide <http://google-styleguide.googlecode.com/svn/trunk/pyguide.html>`_


Django 関連資料
=====================================
次期KawazではDjango 1.3に完全移行する予定なのでドキュメントに目を通すこと。特に
`Class-based generic view <https://docs.djangoproject.com/en/1.3/topics/class-based-views/>`_, 
`The staticfiles app <https://docs.djangoproject.com/en/1.3/ref/contrib/staticfiles/>`_および
`Logging <https://docs.djangoproject.com/en/1.3/topics/logging/>`_は大きな変更もしくは新しい考え方
として加わった部分なので**必ず目を通す**こと。また以下に挙げているライブラリーで使い方がわからない物に関しては
一度は目を通すこと。

-	`Django 1.3 Documentation <https://docs.djangoproject.com/en/1.3/>`_
-	`Django-piston Documentation <https://bitbucket.org/jespern/django-piston/wiki/Documentation#!piston-documentation>`_
-	`Django-pagination Screencast <http://eflorenzano.com/blog/post/first-two-django-screencasts/#using-django-pagination>`_
-	`Django-haystack Documentation <http://docs.haystacksearch.org/dev/>`_
-	`Django-compress Documentation <http://code.google.com/p/django-compress/>`_
-	`Django-reversetag Documentation <https://github.com/ulope/django-reversetag/blob/master/README.rst>`_
-	`Django-markupfield Documentation <http://pypi.python.org/pypi/django-markupfield>`_
-	`Django-filter Documentation <https://github.com/alex/django-filter>`_
-	`Django-mfw Documentation <https://github.com/lambdalisue/django-mfw>`_
-	`Django-qwert Documentation <https://github.com/lambdalisue/django-qwert>`_
-	`Django-object-permission Documentation <https://github.com/lambdalisue/django-object-permission>`_
-	`Django-modify-history Documentation <https://github.com/lambdalisue/django-modify-history>`_
-	`Django-universaltag Documentation <https://github.com/lambdalisue/django-universaltag>`_
-	`Django-googlemap Documentation <https://github.com/lambdalisue/django-googlemap>`_


HTML5 関連資料
======================================
次期Kawazは完全HTML5+CSS3に移行予定なので以下の資料に関しても目を通しておくこと。

-	`HTML5におけるHTML4からの変更点 <http://standards.mitsue.co.jp/resources/w3c/TR/html5-diff/>`_
-	`HTML5タグリファレンス <http://www.html5.jp/tag/elements/index.html>`_
-	`HTML5リファレンス <http://www.htmq.com/html5/index.shtml>`_
-	`CSS3リファレンス <http://www.htmq.com/css3/index.shtml>`_


JavaScript 関連資料
======================================
次期Kawazでも引き続きjQueryを利用する。以下使用方法がわからない場合は目を通すこと。

-	`jQuery <http://docs.jquery.com/Main_Page>`_
-	`jQuery UI <http://jqueryui.com/demos/>`_


テスト用サプリメント集
======================================
テストなどを書く場合に利用できる長文などの便利リンク集

-	｀面白い長文コピペ貼るスレ <http://jbbs.livedoor.jp/game/36824/storage/1198134026.html>`_
-	`おすすめ2ch長文コピペ <http://d.hatena.ne.jp/maname/20071122>`_
