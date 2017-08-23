#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from xml.parsers.expat import ParserCreate

import re

class DefaultSaxHandler(object):
	def start_element(self , name , attrs):
		print 'sax:start_element: %s , attrs: %s' % (name , str(attrs)) 

	def end_element(self , name):
		print 'sax:end_element: %s' % name

	def char_data(self , text):
		print 'sax:char_data: %s' % text

xml = r'''<?xml version="1.0"?> 
<ol>
	<li><a href="/python">Python</a></li>
	<li><a href="/ruby">Ruby</a></li>
</ol>
'''


handler = DefaultSaxHandler()

parsers = ParserCreate()
parsers.returns_unicode = True
parsers.StartElementHandler = handler.start_element
parsers.EndElementHandler = handler.end_element
parsers.CharacterDataHandler = handler.char_data

# parsers.Parse(xml)


# HTMLParser
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

	def __init(self):
		super(MyHTMLParser , self).__init__()

	def handle_starttag(self , tag , attrs):
		self._tag = tag
		self._attrs = attrs	

	def handle_endtag(self , tag):
		pass

	def handle_startendtag(self , tag , attrs):
		pass

	def handle_data(self , data):
		if len(self._attrs):
			value = self._attrs[0][1]
			key = self._attrs[0][0]

			if self._tag == 'a' and value.startswith(r"/events/python-events/") and data.strip():
				print '|-----------------------------------------'
				print '| title : %s           ' % data 
			if key == 'datetime':
				print '| date : %s            ' % data
			if value == 'event-location' and data.strip():
				print '| loc : %s             ' % data


	def handle_comment(self , data):
		pass
		# print '<!-- -->'

	def handle_entityref(self , name):
		pass
		# print '&%s;' % name

	def handle_charref(self , name):
		pass
		# print '&#%s;' % name

parser = MyHTMLParser()
parser.feed(r'''<body class="python events default-page">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lt IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p><strong>Notice:</strong> Your browser is <em>ancient</em> and <a href="http://www.ie6countdown.com/">Microsoft agrees</a>. <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience a better web.</p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">

                
                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>

                
                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>▼</span></span> Close
                </a>

                

<ul class="menu" role="tree">
    
    <li class="python-meta ">
        <a href="/" title="The Python Programming Language">Python</a>
    </li>
    
    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation">PSF</a>
    </li>
    
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation">Docs</a>
    </li>
    
    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index">PyPI</a>
    </li>
    
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board">Jobs</a>
    </li>
    
    <li class="shop-meta ">
        <a href="/community/" title="Python Community">Community</a>
    </li>
    
</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo@2x.png" alt="python™" width="290" height="82"></a>
                </h1>

                <div class="options-bar do-not-print">

                    
                    <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">≡</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                        <fieldset title="Search Python.org">

                            <span aria-hidden="true" class="icon-search"></span>

                            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field placeholder" placeholder="Search" value="" tabindex="1">

                            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                GO
                            </button>

                            
                            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                        </fieldset>
                    </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                        <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="winkwink-nudgenudge">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger">Socialize</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="http://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="http://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a href="http://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="account-signin">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                
                                <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
                                </ul>
                                
                            </li>
                        </ul>
                    </div>

                </div><!-- end options-bar -->

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">
                    
                        
<ul class="navigation menu" role="menubar" aria-label="Main Navigation">
  
    
    
    <li id="about" class="tier-1 element-1   with-supernav" aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    

                            <li class="tier-2 super-navigation">
                                <h4>Python is a programming language that lets you work more quickly and integrate your systems more effectively.</h4>
                                <p>You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs.  <a href="/about">Learn more about Python.</a>.
                            </p></li></ul>

        
    </li>
    
    
    
    <li id="downloads" class="tier-1 element-2   with-supernav" aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
<!-- download supernav from templates/downloads/supernav.html -->
<li class="tier-2 super-navigation">
    
    <div class="download-os-mac-osx" style="">
        
        <h4>Download for Mac OS X</h4>
        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.6.2/python-3.6.2-macosx10.6.pkg">Python 3.6.2</a>
            <a class="button" href="https://www.python.org/ftp/python/2.7.13/python-2.7.13-macosx10.6.pkg">Python 2.7.13</a>
        </p>
        
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-os-source" style="display: none;">
        
        <h3>Python Source</h3>
        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz">Python 3.6.2</a>
            <a class="button" href="https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz">Python 2.7.13</a>
        </p>
        
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-os-windows" style="display: none;">
        
        <h4>Download for Windows</h4>
        
        <p>
            <a class="button" href="https://www.python.org/ftp/python/3.6.2/python-3.6.2.exe">Python 3.6.2</a>
            <a class="button" href="https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi">Python 2.7.13</a>
        </p>
        <p><strong>Note that Python 3.5+ <em>cannot</em> be used on Windows XP or earlier.</strong></p>
        <p>Not the OS you are looking for? Python can be used on many operating systems and environments. <a href="/downloads/">View the full list of downloads</a>.</p>
    </div>
    
    <div class="download-unknown" style="display: none;">
        <h4>Download Python for Any OS</h4>
        <p>Python can be used on many operating systems and environments.</p>
        <p>
            <a class="button" href="/downloads/operating-systems/">View the full list of downloads</a>
        </p>
    </div>
</li>
</ul>

        
    </li>
    
    
    
    <li id="documentation" class="tier-1 element-3   with-supernav" aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
                            <li class="tier-2 super-navigation">
                                <h4>Python’s standard documentation: download, browse or watch a tutorial.</h4>
                                <p>Get started below, or visit the <a href="/doc/versions/">Documentation page to browse by version</a>. </p>
                                <p class="download-buttons">
                                    <a class="button" href="http://docs.python.org/3/">Python 3.x Docs</a> 
                                    <a class="button" href="http://docs.python.org/2/">Python 2.x Docs</a>
                                </p>
                                <p>See also <a href="https://wiki.python.org/moin/Python2orPython3">Should I use Python 2 or 3</a>? </p>
                            </li></ul>

        
    </li>
    
    
    
    <li id="community" class="tier-1 element-4   with-supernav" aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>
    
                            <li class="tier-2 super-navigation">
                                <h4>The Python Community</h4>
<p>Great software is supported by great people. Our user base is enthusiastic, dedicated to encouraging use of the language, and committed to being diverse and friendly.</p>

<!--
                                <p>Here are some events and groups in your area.</p>
                                <ul class="menu">
                                    <li><time datetime="">9/30<span class="say-no-more">/2012</span></time> <a href="#">Royal Python Society Meetup, Providence RI</a></li>
                                    <li><time datetime="">10/4<span class="say-no-more">/2012</span></time> <a href="#">Python Users Group, Boston MA</a></li>
                                    <li><time datetime="">10/5<span class="say-no-more">/2012</span></time> <a href="#">Python Enthusiasts, Cambridge MA</a></li>
                            </ul>
                            </li>--></li></ul>

        
    </li>
    
    
    
    <li id="success-stories" class="tier-1 element-5   with-supernav" aria-haspopup="true">
        <a href="/about/success/" title="success-stories" class="">Success Stories</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>
    
<!-- successstories supernav from templates/successstories/supernav.html -->
       <li class="tier-2 super-navigation">
            
            <img src="/m/successstories/Lucasfilm_logo.png" alt="Industrial Light &amp; Magic">
            
            <blockquote class="success-quote">
                ILM runs a batch processing environment capable of modeling, rendering and compositing tens of thousands of motion picture frames per day. Thousands of machines running Linux, IRIX, Compaq Tru64, OS X, Solaris, and Windows join together to provide a production pipeline used by ~800 users daily. Speed of development is key, and Python was a faster way to code (and re-code) the programs that control this production pipeline.
            </blockquote>
            <p class="quote-by"><cite>Tim Fortenberry</cite>, <a href="http://www.ilm.com/">Industrial Light &amp; Magic</a></p>

        </li></ul>

        
    </li>
    
    
    
    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    
    
    <li id="events" class="tier-1 element-7   with-supernav" aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>
        
            

<ul class="subnav menu" role="menu" aria-hidden="true">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
<li class="tier-2 super-navigation">Find events from the Python Community around the world!</li></ul>

        
    </li>
    
    
    
    
  
</ul>

                    
                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->
                    
    

                </div>

                
                

             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content with-right-sidebar" role="main">

                    
                    

                    

                    
        
        
        <header class="article-header">
            <h3>from the Python Events Calendar</h3>
        </header>
        
        
        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
                
                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>
                
                <ul class="list-recent-events menu">
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/502/">PyCon APAC 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-08-26T00:00:00+00:00">26 Aug. – 28 Aug. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Kuala Lumpur, Malaysia</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/535/">EuroSciPy 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-08-28T00:00:00+00:00">28 Aug. – 02 Sept. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Erlangen, Germany</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/553/">PyData Delhi 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-09-02T00:00:00+00:00">02 Sept. – 04 Sept. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">New Delhi, India</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/544/">Python Sul</a></h3>
                        <p>
                            
                            
<time datetime="2017-09-08T00:00:00+00:00">08 Sept. – 11 Sept. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Universidade de Caxias do Sul (UCS), Caxias do Sul, Rio Grande do Sul, Brazil</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/551/">PyCon Nigeria 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-09-15T00:00:00+00:00">15 Sept. – 17 Sept. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Lagos, Nigeria</span>
                            
                        </p>
                    </li>
                
                    <li>
                        <h3 class="event-title"><a href="/events/python-events/562/">PyCon FR 2017</a></h3>
                        <p>
                            
                            
<time datetime="2017-09-21T00:00:00+00:00">21 Sept. – 25 Sept. <span class="say-no-more"> 2017</span></time>

                            

                            
                            <span class="event-location">Toulouse, France</span>
                            
                        </p>
                    </li>
                
                </ul>
            </div>

            
            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/530/">PyCon PL 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-08-17T00:00:00+00:00">17 Aug. – 21 Aug. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Hotel Ossa Congress &amp; SPA, Ossa, Poland</span>
                        
                    </p>
                </li>
                
                <li>
                    <h3 class="event-title"><a href="/events/python-events/495/">DjangoCon US 2017</a></h3>
                    <p>
                        
                        
<time datetime="2017-08-13T00:00:00+00:00">13 Aug. – 19 Aug. <span class="say-no-more"> 2017</span></time>

                        
                        
                        
                        <span class="event-location">Spokane, WA, USA</span>
                        
                    </p>
                </li>
                
            </ul>
            
        </div>


                </section>

                
                

                
    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">
                
                
                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>
                
            </ul>
            <h2 class="widget-title">Python Events Calendars</h2>

<br>

<p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>

<p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>

<p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>

<p>Thank you.</p>


	    </div>
        
        
        
        
        
    </aside>



            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">

                    
                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>

                    

<ul class="sitemap navigation menu do-not-print" role="tree" id="container" style="position: relative; height: 1632.48px;">
    
    <li class="tier-1 element-1" style="position: absolute; left: 0px; top: 0px;">
        <a href="/about/">About</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-2" style="position: absolute; left: 136px; top: 0px;">
        <a href="/downloads/">Downloads</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-3" style="position: absolute; left: 0px; top: 383px;">
        <a href="/doc/">Documentation</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner's Guide</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="https://docs.python.org/devguide/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-4" style="position: absolute; left: 273px; top: 383px;">
        <a href="/community/">Community</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>
    
        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>
    
        <li class="tier-2 element-9" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>
    
        <li class="tier-2 element-10" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>
    
        <li class="tier-2 element-11" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-5" style="position: absolute; left: 0px; top: 851px;">
        <a href="/about/success/" title="success-stories">Success Stories</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>
    
        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>
    
        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-6" style="position: absolute; left: 136px; top: 851px;">
        <a href="/blogs/" title="News from around the Python world">News</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-7" style="position: absolute; left: 273px; top: 1066px;">
        <a href="/events/">Events</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>
    
        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>
    
</ul>

        
    </li>
    
    <li class="tier-1 element-8" style="position: absolute; left: 0px; top: 1292px;">
        <a href="/dev/">Contributing</a>
        
            

<ul class="subnav menu">
    
        <li class="tier-2 element-1" role="treeitem"><a href="http://docs.python.org/devguide/" title="">Developer's Guide</a></li>
    
        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>
    
        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>
    
        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>
    
</ul>

        
    </li>
    
</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>▲</span></span> Back to Top</a>
                    

                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">
                    
                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/" title="All Systems Operational">Status <span class="python-status-indicator-none" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright ©2001-2017.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->

    
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>

    <script type="text/javascript" src="/static/js/main-min.js" charset="utf-8"></script>
    

    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.js" charset="utf-8"></script>
    
    
    <![endif]-->

    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.js" charset="utf-8"></script>
    
    
    <![endif]-->

    

    
    



</body>''')


