"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
from app.models import PropertyDisplay
from app.forms import PropertyForm


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jada-Ann Vite")

#Upload folder route
@app.route('/uploads/<filename>')
def get_image(filename):
    image_dir = os.getcwd
    return send_from_directory(os.path.join(image_dir,app.config['UPLOAD_FOLDER']), filename)

#route to view form and accept user input
@app.route('/properties/create', methods=['GET','POST'])
def propertyform():
    form = PropertyForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        propertytype = form.propertytype.data
        description = form.description.data
        image = form.image.data

        #save photo to uploads folder 
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #save information to database
        new_property = PropertyDisplay(title=title, bedrooms=bedrooms,bathrooms=bathrooms, location=location, price=price, propertytype=propertytype, description=description, image=filename)
        db.session.add(new_property)
        db.session.commit()

        #redirect to /properties
        flash('New property successfully added.', 'success')
        return redirect(url_for('properties'))
    
    return render_template('propertyform.html' ,form=form)

#view all properties in a database
@app.route('/properties')
def properties():
    property = PropertyDisplay.query.all()
    return render_template('allproperties.html', property=property)

#view property based on id
@app.route('/properties/<int:propertyid>')
def property_search(propertyid):
    indproperty= PropertyDisplay.query.filter_by(id = str(propertyid)).first()
    return render_template('indproperty.html', indproperty=indproperty)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
