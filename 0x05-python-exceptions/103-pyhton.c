#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: PyObject list object.
 * Return: if p is not a valid PyObject,
 * print error  message.
 */
void print_python_list(PyObject *p)
{

