Collecting scipy
  Using cached scipy-0.16.1.tar.gz
    Complete output from command python setup.py egg_info:
    non-existing path in 'numpy/distutils': 'site.cfg'
    Could not locate executable gfortran
    Could not locate executable f95
    Could not locate executable ifort
    Could not locate executable ifc
    Could not locate executable lf95
    Could not locate executable pgfortran
    Could not locate executable f90
    Could not locate executable f77
    Could not locate executable fort
    Could not locate executable efort
    Could not locate executable efc
    Could not locate executable g77
    Could not locate executable g95
    Could not locate executable pathf95
    don't know how to compile Fortran code on platform 'posix'
    _configtest.c:1:5: warning: conflicting types for built-in function ‘exp’
     int exp (void);
         ^
    _configtest.o: In function `main':
    /tmp/easy_install-vb_87knz/numpy-1.10.2/_configtest.c:6: undefined reference to `exp'
    collect2: error: ld returned 1 exit status
    _configtest.c:1:5: warning: conflicting types for built-in function ‘exp’
     int exp (void);
         ^
    _configtest.c:1:20: fatal error: Python.h: Arquivo ou diretório não encontrado
     #include <Python.h>
                        ^
    compilation terminated.
    Running from numpy source directory.
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1651: UserWarning:
        Atlas (http://math-atlas.sourceforge.net/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [atlas]) or by setting
        the ATLAS environment variable.
      warnings.warn(AtlasNotFoundError.__doc__)
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1660: UserWarning:
        Blas (http://www.netlib.org/blas/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [blas]) or by setting
        the BLAS environment variable.
      warnings.warn(BlasNotFoundError.__doc__)
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1663: UserWarning:
        Blas (http://www.netlib.org/blas/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [blas_src]) or by setting
        the BLAS_SRC environment variable.
      warnings.warn(BlasSrcNotFoundError.__doc__)
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1552: UserWarning:
        Atlas (http://math-atlas.sourceforge.net/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [atlas]) or by setting
        the ATLAS environment variable.
      warnings.warn(AtlasNotFoundError.__doc__)
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1563: UserWarning:
        Lapack (http://www.netlib.org/lapack/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [lapack]) or by setting
        the LAPACK environment variable.
      warnings.warn(LapackNotFoundError.__doc__)
    /tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/system_info.py:1566: UserWarning:
        Lapack (http://www.netlib.org/lapack/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [lapack_src]) or by setting
        the LAPACK_SRC environment variable.
      warnings.warn(LapackSrcNotFoundError.__doc__)
    /usr/lib/python3.4/distutils/dist.py:260: UserWarning: Unknown distribution option: 'define_macros'
      warnings.warn(msg)
    Traceback (most recent call last):
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 152, in save_modules
        yield saved
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 193, in setup_context
        yield
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 237, in run_setup
        DirectorySandbox(setup_dir).run(runner)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 267, in run
        return func()
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 236, in runner
        _execfile(setup_script, ns)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 46, in _execfile
        exec(code, globals, locals)
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/setup.py", line 263, in <module>
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/setup.py", line 255, in setup_package
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/core.py", line 169, in setup
      File "/usr/lib/python3.4/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/usr/lib/python3.4/distutils/dist.py", line 955, in run_commands
        self.run_command(cmd)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/bdist_egg.py", line 151, in run
        self.run_command("egg_info")
      File "/usr/lib/python3.4/distutils/cmd.py", line 313, in run_command
        self.distribution.run_command(command)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/egg_info.py", line 10, in run
      File "/usr/lib/python3.4/distutils/cmd.py", line 313, in run_command
        self.distribution.run_command(command)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 153, in run
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 170, in build_sources
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 329, in build_extension_sources
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 386, in generate_sources
      File "numpy/core/setup.py", line 417, in generate_config_h
      File "numpy/core/setup.py", line 42, in check_types
        Topic :: Software Development
      File "numpy/core/setup.py", line 278, in check_types
    SystemError: Cannot compile 'Python.h'. Perhaps you need to install python-dev|python-devel.
    
    During handling of the above exception, another exception occurred:
    
    Traceback (most recent call last):
      File "<string>", line 20, in <module>
      File "/tmp/pip-build-4q_8_6du/scipy/setup.py", line 253, in <module>
        setup_package()
      File "/tmp/pip-build-4q_8_6du/scipy/setup.py", line 250, in setup_package
        setup(**metadata)
      File "/usr/lib/python3.4/distutils/core.py", line 108, in setup
        _setup_distribution = dist = klass(attrs)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/dist.py", line 268, in __init__
        self.fetch_build_eggs(attrs['setup_requires'])
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/dist.py", line 313, in fetch_build_eggs
        replace_conflicting=True,
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/pkg_resources/__init__.py", line 843, in resolve
        dist = best[req.key] = env.best_match(req, ws, installer)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/pkg_resources/__init__.py", line 1088, in best_match
        return self.obtain(req, installer)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/pkg_resources/__init__.py", line 1100, in obtain
        return installer(requirement)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/dist.py", line 380, in fetch_build_egg
        return cmd.easy_install(req)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/easy_install.py", line 638, in easy_install
        return self.install_item(spec, dist.location, tmpdir, deps)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/easy_install.py", line 668, in install_item
        dists = self.install_eggs(spec, download, tmpdir)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/easy_install.py", line 851, in install_eggs
        return self.build_and_install(setup_script, setup_base)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/easy_install.py", line 1079, in build_and_install
        self.run_setup(setup_script, setup_base, args)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/easy_install.py", line 1065, in run_setup
        run_setup(setup_script, args)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 240, in run_setup
        raise
      File "/usr/lib/python3.4/contextlib.py", line 77, in __exit__
        self.gen.throw(type, value, traceback)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 193, in setup_context
        yield
      File "/usr/lib/python3.4/contextlib.py", line 77, in __exit__
        self.gen.throw(type, value, traceback)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 164, in save_modules
        saved_exc.resume()
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 139, in resume
        compat.reraise(type, exc, self._tb)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/compat.py", line 65, in reraise
        raise value.with_traceback(tb)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 152, in save_modules
        yield saved
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 193, in setup_context
        yield
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 237, in run_setup
        DirectorySandbox(setup_dir).run(runner)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 267, in run
        return func()
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 236, in runner
        _execfile(setup_script, ns)
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/sandbox.py", line 46, in _execfile
        exec(code, globals, locals)
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/setup.py", line 263, in <module>
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/setup.py", line 255, in setup_package
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/core.py", line 169, in setup
      File "/usr/lib/python3.4/distutils/core.py", line 148, in setup
        dist.run_commands()
      File "/usr/lib/python3.4/distutils/dist.py", line 955, in run_commands
        self.run_command(cmd)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/home/allan/GDSW/matricula/env/lib/python3.4/site-packages/setuptools/command/bdist_egg.py", line 151, in run
        self.run_command("egg_info")
      File "/usr/lib/python3.4/distutils/cmd.py", line 313, in run_command
        self.distribution.run_command(command)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/egg_info.py", line 10, in run
      File "/usr/lib/python3.4/distutils/cmd.py", line 313, in run_command
        self.distribution.run_command(command)
      File "/usr/lib/python3.4/distutils/dist.py", line 974, in run_command
        cmd_obj.run()
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 153, in run
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 170, in build_sources
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 329, in build_extension_sources
      File "/tmp/easy_install-vb_87knz/numpy-1.10.2/numpy/distutils/command/build_src.py", line 386, in generate_sources
      File "numpy/core/setup.py", line 417, in generate_config_h
      File "numpy/core/setup.py", line 42, in check_types
        Topic :: Software Development
      File "numpy/core/setup.py", line 278, in check_types
    SystemError: Cannot compile 'Python.h'. Perhaps you need to install python-dev|python-devel.
    _configtest.o: In function `main':
    /tmp/easy_install-vb_87knz/numpy-1.10.2/_configtest.c:6: undefined reference to `exp'
    collect2: error: ld returned 1 exit status
    _configtest.c:1:20: fatal error: Python.h: Arquivo ou diretÃ³rio nÃ£o encontrado
     #include <Python.h>
                        ^
    compilation terminated.
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-4q_8_6du/scipy
