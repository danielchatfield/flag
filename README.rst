flag
====

A golang inspired simple flag library for python.

Installation
------------

To install flag, simply:

.. code-block:: bash

    $ pip install flag


Usage
-----

.. code-block:: python

    import flag

    num_workers = flag.int("workers", 10, "Number of worker threads")


    if __name__ == '__main__':
        flag.parse()

    print("Num workers %d" % num_workers)
