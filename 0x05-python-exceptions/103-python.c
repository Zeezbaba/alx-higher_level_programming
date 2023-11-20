#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", PyList_Size(p));

    PyObject *item;
    Py_ssize_t i;

    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < PyList_Size(p); ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}


/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");

    printf("  size: %zd\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    if (PyBytes_Size(p) < 10)
        printf("  first %zd bytes: %s\n", PyBytes_Size(p) + 1, PyBytes_AsString(p));
    else
        printf("  first 10 bytes: %s\n", PyBytes_AsString(p));
}


/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");

    if (PyFloat_IS_INTEGER(p))
        printf("  value: %0.1f\n", PyFloat_AS_DOUBLE(p));
    else
        printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
}
