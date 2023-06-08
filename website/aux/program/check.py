import pkgutil

package_name = 'program'  # Replace with your package name
is_package = pkgutil.get_loader(package_name) is not None

if is_package:
    print(f"The folder '{package_name}' is recognized as a package.")
else:
    print(f"The folder '{package_name}' is not recognized as a package.")