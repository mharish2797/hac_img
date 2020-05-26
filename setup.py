import setuptools

setuptools.setup(
        name='hac-img',
		packages = ['hac-img'],
        version='0.0.1',
		license='MIT',
        description='Hierarchical clustering algorithm for image clustering using Scikit-Image',
		author = 'Harish Mohan',                   # Type in your name
		author_email = 'mharish2797@gmail.com',      # Type in your E-Mail
		url = 'https://mharish.dev',   # Provide either the link to your github or to your website
		download_url = 'https://github.com/mharish2797/hac_img/archive/0.0.1.tar.gz',    # I explain this later on
		keywords = ['image', 'hierarchical', 'clustering'],   # Keywords that define your package best
        py_modules=["hac_img"],
        install_requires = ["scikit-image", "numpy", "Pillow"]
		
        )